from pymongo import MongoClient
from bson import ObjectId,errors
from dotenv import load_dotenv
import os

load_dotenv() #Loads variables from .env
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI) #ytmanager is the name of the database

db = client["ytmanager"] #name of db
video_collection = db["videos"] #for collections in database

#print(video_collection)

def list_videos():
    if video_collection.count_documents({}) == 0:
        print("No Videos Available to Show!!")
        return
    print("The current videos in the database:-")
    print("-"*50)
    for video in video_collection.find():
        print(f"ID: {video['_id']} \n Name: {video['name']} \n Time: {video['time']}")  #in mongodb, ID is specified as '_id'
    print("-"*50)

def add_video(name,time):
    if not name or not time:
        print("Name and Time duration are required!!")
    try:
        video_collection.insert_one({"name":name,"time":time})
        print("Video added successfully!")
    except Exception as e:
        print(f"Exception occured: \n {e}")
    
def update_video(video_id,new_name,new_time):
    try:
        result = video_collection.update_one(
            {'_id':ObjectId(video_id)}, 
            {"$set":{"name":new_name, "time":new_time}}
        )
        print(result)
        if result.matched_count == 0:
            print("No video found with that ID")
        else:
            print("The video was updated successfully!!")
    except errors.InvalidId:
        print("Invalid ID format.")
    except Exception as e:
        print(f"Exception Occured:\n {e}")
        
def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id":ObjectId(video_id)})
        if result.deleted_count == 0:
            print("No video found with that ID")
        else:
            print("The video was deleted Successfully!!")
    except errors.InvalidId:
        print("Invalid ID format")
    except Exception as e:
        print(f"Exception has occured:\n {e}")
    

def main():
    while True:
        print("\n YouTube manager App")
        print("1.List all videos")
        print("2.Add new video")
        print("3.Update a video")
        print("4.Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the name: ")
            time = input("Enter the duration: ")
            add_video(name,time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated duration: ")
            update_video(video_id,name,time)
        elif choice == "4":
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Thanks for using the Youtube manager app!")
            break
        else:
            print("Invalid Choice!!")
        

if __name__ == "__main__":
    main()