import profiles from "./data"
import Gallery from "./components/Gallery"

function App() {
    return (
        <div className="app">
            <header className="header">
                <h1>👥 Profile Gallery</h1>
                <p>{profiles.length} team members</p>
            </header>
            <Gallery profiles={profiles} />
        </div>
    )
}

export default App