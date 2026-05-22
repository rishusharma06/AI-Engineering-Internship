import { useState, useEffect } from "react"

//the Typing component internal
function Typing() {
    const [text, setText] = useState("")

    return (
        <div style={{padding: "50px", textAlign: "center"}}>
            <input
                type="text"
                placeholder="type something here..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                style={{padding: "10px", fontSize: "16px", width: "300px"}}
            />
            <p>You Typed: <strong>{text}</strong></p>
            <p>Characters: {text.length}</p>
            {text.length > 20 && <p style={{color: "red"}}>Very Long!</p>}
        </div>
    )
}

function Timer() {
    const [seconds, setSeconds] = useState(0)

    useEffect(() => {
        // Timer shuru karo
        const interval = setInterval(() => {
            setSeconds(prev => prev + 1)
        }, 1000)

        // Cleanup — component unmount hone pe timer band karo
        return () => clearInterval(interval)
    }, [])  // sirf ek baar shuru karo

    return <h1>⏱️ {seconds} seconds</h1>
}


//Main App component that displays both features
function App() {
    const [count, setCount] = useState(0)

    return (
        <div style={{textAlign: "center", padding: "50px"}}>
            <h1>Counter: {count}</h1>

            <button
                onClick={() => setCount(count + 1)}
                style={{margin: "5px", padding: "10px 20px"}}
            >
                +1
            </button>

            <button
                onClick={() => setCount(count - 1)}
                style={{margin: "5px", padding: "10px 20px"}}
            >
                -1
            </button>

            <button
                onClick={() => setCount(0)}
                style={{margin: "5px", padding: "10px 20px"}}
            >
                Reset
            </button>

            <p style={{marginTop: "20px", color: count > 0 ? "green" : count < 0 ? "red" : "black"}}>
                {count > 0 ? "Positive!" : count < 0 ? "Negative!" : "Zero!"}
            </p>

            <hr style={{margin: "40px 0", borderColor: "#eee"}} />

            {/* Rendering the Typing component here */}
            <Typing />
            <hr style={{margin: "40px 0", borderColor: "#eee"}} />

            {/* Rendering the Timer component here */}
            <Timer />
        </div>
    )
}

//Only ONE default export
export default App;
