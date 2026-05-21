import Card from "./Card"

function Gallery({ profiles }) {
    return (
        <div className="gallery">
            {profiles.map((profile) => (
                <Card
                    key={profile.id}
                    name={profile.name}
                    role={profile.role}
                    city={profile.city}
                    image={profile.image}
                    skills={profile.skills}
                />
            ))}
        </div>
    )
}

export default Gallery