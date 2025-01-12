import json
import urllib.request


def processing_event(event: str) -> None:
    if event["type"] == "PushEvent":
        print(f"- pushed {event['payload']['size']} commits to {event['repo']['name']}")
    elif event["type"] == "IssuesEvent":
        print(f"- {event['payload']['action']} a issue in {event['repo']['name']}")
    elif event["type"] == "WatchEvent":
        print(f"- starred {event['repo']['name']}")
    elif event["type"] == "CreateEvent":
        print(
            f"- created a new {event['payload']['ref_type']} in {event['repo']['name']}"
        )
    elif event["type"] == "PullRequestEvent":
        print(
            f"- {event['payload']['action']} a pullrequest in {event['repo']['name']}"
        )
    elif event["type"] == "DeleteEvent":
        print(f"- delete a {event['payload']['ref_type']} in {event['repo']['name']}")
    elif event["type"] == "ForkEvent":
        print(f"- fork a {event['payload']['ref_type']} in {event['repo']['name']}")
    elif event["type"] == "CommitCommentEvent":
        print(f"- Created a comment on {event['repo']['name']}")
    elif event["type"] == "IssueCommentEvent":
        print(f"- {event['payload']['action']} a issue in {event['repo']['name']}")
    elif event["type"] == "PullRequestReviewEvent":
        print(f"- created a pullrequest review in {event['repo']['name']}")
    elif event["type"] == "PullRequestReviewCommentEvent":
        print(f"- commented on a pullrequst review in {event['repo']['name']}")
    elif event["type"] == "PullRequestReviewThreadEvent":
        print(
            f"- marked {event['payload']['action']} for a pull request comment in {event['repo']['name']}"
        )
    elif event["type"] == "MemberEvent":
        print(f"- added {event['payload']['member']} to {event['repo']['name']}")
    elif event["type"] == "MemberEvent":
        print(f"- made {event['repo']['name']} public")
    else:
        print(event)


if __name__ == "__main__":
    user2 = "kamranahmedse"
    user3 = "XYZ-qiyh"
    user = "MarkLLLuo"
    try:
        with urllib.request.urlopen(f"https://api.github.com/users/{user}/events") as f:
            content = f.read()
            events = json.loads(content.decode("utf-8"))
            num = len(events)
            print(f"{num}")
            if num > 0:
                print(f"{num} OUTPUT found for user: {events[0]['actor']['login']}:")
                for event in events:
                    processing_event(event)
            else:
                print(f"NO RESULT FOUND FOR {user}")
    except urllib.error.HTTPError as e:
        print(f"Invalid request, error code: {e.code}")
