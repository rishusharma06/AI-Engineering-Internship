from agent.graph import graph

while True:
    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    result = graph.invoke({
        "question": question,
        "context": [],
        "answer": ""
    })

    print("\nAnswer:\n")
    print(result["answer"])