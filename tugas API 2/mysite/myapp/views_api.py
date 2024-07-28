# myapp/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Course, User
import json
import requests

def json_response(data, status=200):
    return JsonResponse(data, safe=False, status=status)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def apiCourse(request):
    if request.method == "GET":
        courses = list(Course.objects.values())
        return json_response(courses)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            course = Course.objects.create(
                course_name=data["course_name"],
                course_created_by=data["course_created_by"]
            )
            return json_response({"message": "Course created", "course_id": course.course_id}, status=201)
        except KeyError as e:
            return json_response({"error": f"Missing key: {str(e)}"}, status=400)
        except Exception as e:
            return json_response({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def updateCourseApi(request, id):
    try:
        course = Course.objects.get(course_id=id)
        data = json.loads(request.body)
        course.course_name = data.get("course_name", course.course_name)
        course.course_updated_by = data.get("course_updated_by", course.course_updated_by)
        course.save()
        return json_response({"message": "Course updated"})
    except Course.DoesNotExist:
        return json_response({"message": "Course not found"}, status=404)
    except KeyError as e:
        return json_response({"error": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        return json_response({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def deleteCourseApi(request, id):
    try:
        course = Course.objects.get(course_id=id)
        course.delete()
        return json_response({"message": "Course deleted"})
    except Course.DoesNotExist:
        return json_response({"message": "Course not found"}, status=404)
    except Exception as e:
        return json_response({"error": str(e)}, status=500)

@csrf_exempt
def consume_api_get(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
        local_users = list(User.objects.values())
        combined_data = data + local_users
        return render(request, "api_get.html", {'data': combined_data})
    except requests.exceptions.RequestException as e:
        return json_response({"error": str(e)}, status=500)
    except Exception as e:
        return json_response({"error": str(e)}, status=500)

@csrf_exempt
def create_user(request):
    try:
        # Dapatkan data dari placeholder API
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        placeholder_data = response.json()
        
        # Tentukan ID baru
        last_id_placeholder = max(user['id'] for user in placeholder_data)
        last_id_local = User.objects.order_by('-id').first().id if User.objects.exists() else 0
        new_id = max(last_id_placeholder, last_id_local) + 1
        
        # Parsing data request
        data = json.loads(request.body)
        
        # Buat objek User baru
        user = User(
            id=new_id,
            name=data["name"],
            username=data["username"],
            email=data["email"],
            street=data["address"]["street"],
            suite=data["address"]["suite"],
            city=data["address"]["city"],
            zipcode=data["address"]["zipcode"],
            geo_lat=data["address"]["geo"]["lat"],
            geo_lng=data["address"]["geo"]["lng"],
            phone=data["phone"],
            website=data["website"],
            company_name=data["company"]["name"],
            company_catchPhrase=data["company"]["catchPhrase"],
            company_bs=data["company"]["bs"]
        )
        user.save()
        
        return JsonResponse({"message": "User created", "user_id": user.id}, status=201)
    except KeyError as e:
        return JsonResponse({"error": f"Missing key: {str(e)}"}, status=400)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
 

@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
        data = json.loads(request.body)
        user.name = data.get("name", user.name)
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.street = data["address"].get("street", user.street)
        user.suite = data["address"].get("suite", user.suite)
        user.city = data["address"].get("city", user.city)
        user.zipcode = data["address"].get("zipcode", user.zipcode)
        user.geo_lat = data["address"]["geo"].get("lat", user.geo_lat)
        user.geo_lng = data["address"]["geo"].get("lng", user.geo_lng)
        user.phone = data.get("phone", user.phone)
        user.website = data.get("website", user.website)
        user.company_name = data["company"].get("name", user.company_name)
        user.company_catchPhrase = data["company"].get("catchPhrase", user.company_catchPhrase)
        user.company_bs = data["company"].get("bs", user.company_bs)
        user.save()
        return json_response({"message": "User updated"}, status=200)
    except User.DoesNotExist:
        return json_response({"message": "User not found"}, status=404)
    except KeyError as e:
        return json_response({"error": f"Missing key: {str(e)}"}, status=400)
    except Exception as e:
        return json_response({"error": str(e)}, status=500)
