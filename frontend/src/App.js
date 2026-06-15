import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [description, setDescription] = useState("");
  const [result, setResult] = useState(null);

  const analyzeResume = async () => {
    if (!file) {
      alert("Please upload a resume");
      return;
    }

    if (!description) {
      alert("Please enter job description");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/ai-review?description=" + description,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);
    } catch (error) {
      console.log(error);
      alert("Backend connection failed");
    }
  };

  return (
    <div style={{ textAlign: "center", margin: "30px" }}>
      <h1>AI Resume Matcher</h1>

      <h2>Upload Resume</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <h2>Job Description</h2>

      <textarea
        rows="10"
        cols="80"
        placeholder="Paste Job Description Here"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <br />
      <br />

      <button onClick={analyzeResume}>
        Analyze Resume
      </button>

      <hr />

      <h1>Results</h1>

      {result && (
        <div style={{ textAlign: "left", margin: "20px auto", width: "80%" }}>

          <h3>ATS Result</h3>
          <p>{result.ATS_Result}</p><br></br>

          <h3>Match Score</h3>
          <p>{result.Match_Score}%</p><br></br>

          <h3>Matched Skills</h3>
          <ul>
            {result.Matched_Skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul><br></br>

          <h3>Missing Skills</h3>
          <ul>
            {result.Missing_Skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul><br></br>

          <h3>Strengths</h3>
          <ul>
            {result.Strengths.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul><br></br>

          <h3>Weaknesses</h3>
          <ul>
            {result.Weaknesses.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul><br></br>

          <h3>Suggestions</h3>
          <ul>
            {result.Suggestions.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul><br></br>

          <h3>Project Ideas</h3>
          <ul>
            {result.Project_Ideas.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul><br></br>

          <h3>Final Recommendation</h3>
          <p>{result.Final_Recommendation}</p>

        </div>
      )}
    </div>
  );
}

export default App;