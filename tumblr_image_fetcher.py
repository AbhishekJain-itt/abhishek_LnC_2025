import json
import requests

PHOTO_POST_LIMIT = 50
PHOTO_QUALITY_WIDTH = 1280
TUMBLR_API_JS_PREFIX = "var tumblr_api_read = "

def read_user_input():
    """
    Reads and validates user input.
    Returns:
        blog_name (str)
        start_post (int)
        end_post (int)
    """
    blog_name = input("Enter the Tumblr blog name:\n").strip()

    if not blog_name:
        raise ValueError("Blog name cannot be empty")

    post_range = input("Enter the range (start-end):\n").strip()

    try:
        start_post, end_post = map(int, post_range.split("-"))
    except ValueError:
        raise ValueError("Range must be in start-end format")

    if start_post < 1 or end_post < start_post:
        raise ValueError("Invalid post range")

    return blog_name, start_post, end_post


# Tumblr API Handling

def fetch_tumblr_photo_posts(blog_name):
    """
    Fetches Tumblr photo posts using API v1.
    Safely extracts JSON from JavaScript response.
    """
    api_url = (
        f"https://{blog_name}.tumblr.com/api/read/json"
        f"?type=photo&num={PHOTO_POST_LIMIT}"
    )

    response = requests.get(api_url, timeout=10)

    if response.status_code != 200:
        raise ConnectionError("Unable to reach Tumblr API")

    response_text = response.text

    # Tumblr API v1 wraps JSON inside JavaScript.
    # Extract only the JSON object between first '{' and last '}'.
    json_start = response_text.find("{")
    json_end = response_text.rfind("}") + 1

    if json_start == -1 or json_end == -1:
        raise ValueError("Invalid Tumblr API response format")

    json_payload = response_text[json_start:json_end]

    return json.loads(json_payload)




def print_blog_metadata(api_response):
    """
    Prints basic blog information.
    """
    blog_info = api_response.get("tumblelog", {})

    print("\n---------------------------------------")
    print("title:", blog_info.get("title", ""))
    print("name:", blog_info.get("name", ""))
    print("description:", blog_info.get("description", ""))
    print("no of post:", api_response.get("posts-total", 0))
    print("---------------------------------------\n")


def print_images_by_post(api_response, start_post, end_post):
    """
    Prints highest-quality images (1280) for each post
    in the given post range using Tumblr API v1 structure.
    """
    posts = api_response.get("posts", [])

    start_index = start_post - 1
    end_index = min(end_post, len(posts))

    for index in range(start_index, end_index):
        post = posts[index]

        print(f"{index + 1}.")

        # 1: Single image post
        if "photo-url-1280" in post:
            print("   " + post["photo-url-1280"])

        # 2: Multiple images (photoset)
        elif "photoset" in post:
            for photo in post["photoset"]:
                if "photo-url-1280" in photo:
                    print("   " + photo["photo-url-1280"])

        print()


def print_high_quality_image(photo):
    """
    Prints only the highest resolution image
    from a photo object.
    """
    for image in photo.get("photo-urls", []):
        if image.get("max-width") == PHOTO_QUALITY_WIDTH:
            print("   " + image.get("url"))


def main():
    """
    Orchestrates program execution.
    """
    try:
        blog_name, start_post, end_post = read_user_input()
        api_response = fetch_tumblr_photo_posts(blog_name)

        print_blog_metadata(api_response)
        print_images_by_post(api_response, start_post, end_post)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
