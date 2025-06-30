course = c











    "shortLink": "toplearn.com/c
    
    
    /o2V3",
    "sessions": [
        {
            "title": "sessions-1"
            "time": 5
        },
    {
            "title": "sessions-2"
            "time": 7
        },
    {
            "title": "sessions-3"
            "time": 9
        }
    ],
    "relatedCourses": [
        
    ]









fuck
for related in course["relatesCourses"]:
    print(related["title"])
    
total_time = 0 
for session in course["sessions"]:
    total_time +=session["time"]
    
print(total_taime)
