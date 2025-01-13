import json
import sys
import urllib.request


def processing_event(event: str) -> None:
    repo_name = event["repo"]["name"]
    if event["type"] == "PushEvent":
        print(f"- pushed {event['payload']['size']} commits to {repo_name}")
    elif event["type"] == "IssuesEvent":
        print(f"- {event['payload']['action']} a issue in {repo_name}")
    elif event["type"] == "WatchEvent":
        print(f"- starred {repo_name}")
    elif event["type"] == "CreateEvent":
        print(f"- created a new {event['payload']['ref_type']} in {repo_name}")
    elif event["type"] == "PullRequestEvent":
        print(f"- {event['payload']['action']} a pullrequest in {repo_name}")
    elif event["type"] == "DeleteEvent":
        print(f"- delete a {event['payload']['ref_type']} in {repo_name}")
    elif event["type"] == "ForkEvent":
        print(f"- fork a {event['payload']['ref_type']} in {repo_name}")
    elif event["type"] == "CommitCommentEvent":
        print(f"- Created a comment on {repo_name}")
    elif event["type"] == "IssueCommentEvent":
        print(f"- {event['payload']['action']} a issue in {repo_name}")
    elif event["type"] == "PullRequestReviewEvent":
        print(f"- created a pullrequest review in {repo_name}")
    elif event["type"] == "PullRequestReviewCommentEvent":
        print(f"- commented on a pullrequst review in {repo_name}")
    elif event["type"] == "PullRequestReviewThreadEvent":
        print(
            f"- marked {event['payload']['action']} for a pull request comment in {repo_name}"
        )
    elif event["type"] == "MemberEvent":
        print(f"- added {event['payload']['member']} to {repo_name}")
    elif event["type"] == "MemberEvent":
        print(f"- made {repo_name} public")
    else:
        print(event)


if __name__ == "__main__":
    user = sys.argv[1]
    if not len(sys.argv) == 2:
        user = input("Invalid username, please try again:")
    try:
        with urllib.request.urlopen(f"https://api.github.com/users/{user}/events") as f:
            content = f.read()
            events = json.loads(content.decode("utf-8"))
            num = len(events)
            if num > 0:
                print(f"{num} OUTPUT found for user: {events[0]['actor']['login']}:")
                for event in events:
                    processing_event(event)
            else:
                print(f"NO RESULT FOUND FOR {user}")
    except urllib.error.HTTPError as e:
        print(f"Invalid request, error code: {e.code}")
