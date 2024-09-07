import json

def load_data():
    try:
        with open('youtube_manager/youtube1.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [1,2]
    
def save_data_helper(videos):
    with open('youtube_manager/youtube1.txt', 'w') as file:
        json.dump(videos, file)
        
    

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index} ")
        print(f"name: {video['name']}, duration: {video['time']} ")

def add_video(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)  
    

def update_video(videos):
    index = int(input("what number of video you want to update"))
    name = input("enter new video name: ")
    time = input("enter new video time: ")
    videos[index-1] = {'name': name, 'time': time}
    save_data_helper(videos)
    

def delete_video(videos):
    videoNum = int(input("enter the index of video you want to be deleted: "))
    del videos[videoNum-1]
    save_data_helper(videos)
    

 
def main():
    videos = load_data()
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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()


