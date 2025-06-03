from collections import deque

# สร้าง stack และ queue
stack = []
queue = deque()

print("คำสั่ง: push X / pop / enqueue X / dequeue / show / exit")

while True:
    command = input(">> ").strip().lower()

    if command.startswith("push "):
        value = command[5:]
        stack.append(value)
        print(f"📦 Push: {value}")

    elif command == "pop":
        if stack:
            popped = stack.pop()
            print(f"🗑️ Pop: {popped}")
        else:
            print("⚠️ Stack ว่าง")

    elif command.startswith("enqueue "):
        value = command[8:]
        queue.append(value)
        print(f"📥 Enqueue: {value}")

    elif command == "dequeue":
        if queue:
            dequeued = queue.popleft()
            print(f"📤 Dequeue: {dequeued}")
        else:
            print("⚠️ Queue ว่าง")

    elif command == "show":
        print(f"🧱 Stack: {stack}")
        print(f"📚 Queue: {list(queue)}")

    elif command == "exit":
        break

    else:
        print("❌ คำสั่งไม่ถูกต้อง")
