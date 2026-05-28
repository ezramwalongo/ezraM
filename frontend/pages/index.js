// pages/index.js
import { useEffect, useState } from "react";

export default function Home() {
  const [portfolio, setPortfolio] = useState(null);

  useEffect(() => {
    fetch("https://ezram-4.onrender.com/") // <-- your Render API endpoint
      .then((res) => res.json())
      .then((data) => setPortfolio(data))
      .catch((err) => console.error("Error fetching portfolio:", err));
  }, []);

  if (!portfolio) {
    return (
      <div className="min-vh-100 d-flex justify-content-center align-items-center bg-dark text-white">
        <h2>Loading Portfolio...</h2>
      </div>
    );
  }

  return (
    <div className="min-vh-100 bg-dark text-white">
      {/* Hero */}
      <header className="text-center py-5 shadow" style={{ backgroundColor: "magenta" }}>
        <h1 className="fw-bold">{portfolio.name}</h1>
        <h3 className="fw-light">{portfolio.title}</h3>
        <p className="mt-3">{portfolio.profile}</p>
      </header>

      <main className="container py-5">
        {/* Skills */}
        <section className="mb-5 text-center">
          <h2 className="text-info mb-3">Skills</h2>
          {portfolio.skills.map((s, i) => (
            <span
              key={i}
              className="badge rounded-pill me-2 mb-2 fs-6 shadow-sm"
              style={{ backgroundColor: "cyan", color: "black" }}
            >
              {s}
            </span>
          ))}
        </section>

        {/* Qualifications */}
        <section className="mb-5">
          <h2 className="text-warning mb-3 text-center">Qualifications</h2>
          <ul className="list-group">
            {portfolio.qualifications.map((q, i) => (
              <li key={i} className="list-group-item bg-dark text-white border-light">
                {q}
              </li>
            ))}
          </ul>
        </section>

        {/* Projects */}
        <section className="mb-5">
          <h2 className="text-success mb-3 text-center">Projects</h2>
          <div className="row">
            {portfolio.projects.map((p, i) => (
              <div key={i} className="col-md-6 mb-4">
                <div className="card h-100 shadow-lg" style={{ backgroundColor: "#0d6efd", color: "white" }}>
                  <div className="card-body">
                    <h5 className="card-title fw-bold">{p.title}</h5>
                    <p className="card-text">{p.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Contact */}
        <section className="text-center">
          <h2 className="text-danger mb-3">Contact</h2>
          <p>Email: {portfolio.contact.email}</p>
          <p>Phone: {portfolio.contact.phone}</p>
          <p>Location: {portfolio.contact.location}</p>
        </section>
      </main>

      <footer className="text-center py-3 bg-secondary text-white">
        <small>&copy; {new Date().getFullYear()} {portfolio.name} | Professional Portfolio</small>
      </footer>
    </div>
  );
}

