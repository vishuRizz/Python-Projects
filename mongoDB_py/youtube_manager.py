from pymongo import MongoClient

client = MongoClient("mongodb+srv://vishurizz01:RzfgxKDYAOSSooKq@cluster0.7ozbuch.mongodb.net/", tlsAllowInvalidCertificates = True)
db = client['py_yt_manager']
video_collection = db['videos']
def list_all_videos():
    for video in video_collection.find():
        print(f"id: {video['_id']}, 'name':{video['title']}, 'time': {video['time']}")
        
def add_video():
    title = input("Enter video title: ")
    time = input("enter video time: ")
    video_collection.insert_one({"title": title, "time": time})

    
def update_video():
    video_id = input("enter videoId for update")
    name = input("Enter video title: ")
    time = input("enter video time: ")

def delete_video():
    video_id = input("enter videoId for delete")
    # video_collection.delete_one({"_id": video_id})
    print("Video deleted successfully")
    
def main():
   
    while True:
        print("\n youtube manager | make your choice")
        print("1. list all youtube videos")
        print("2. add a youtube video")
        print("3. update a youtube video details")
        print("4. delete a youtube videos")
        print("5. exit the app")
        choice = input("enter your choice:  ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()


