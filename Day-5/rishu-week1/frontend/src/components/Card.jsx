function Card({ name, email, company, website }) {
  return (
    <div className="card">
      <h3>{name}</h3>

      <p>
        <span>Email:</span> {email}
      </p>

      <p>
        <span>Company:</span> {company}
      </p>

      <p>
        <span>Website:</span> {website}
      </p>
    </div>
  );
}

export default Card;