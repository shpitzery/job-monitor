function JobList({ jobs }) {
    const dateForm = (postedDate) => {
        // Extract only the date part
        const dateStr = postedDate.toLowerCase().startsWith('posted') ? postedDate.slice(7) : postedDate;

        const date = new Date(dateStr);

        // Get the short month name
        const month = date.toLocaleString('en-US', { month: 'short' });

        // Get day and year
        const day = date.getDate();
        const year = date.getFullYear();

        return `Posted ${month} ${day}, ${year}`;
    }

  return (
    <div style={{ width: "80%", margin: "auto" }}>
      <h2 style={{ textAlign: "center", marginBottom: "20px" }}>Featured Jobs</h2>
      <div style={{
        border: "1px solid #ddd",
        borderRadius: "10px",
        overflow: "hidden",
      }}>
        {jobs.map((job, index) => (
          <div key={index} style={{
            display: "flex",
            alignItems: "center",
            padding: "20px",
            borderBottom: "1px solid #ddd",
            backgroundColor: index % 2 === 0 ? "#fff" : "#f9f9f9",
            // gap: "24px",
            fontSize: "16px",
            paddingTop: "20px",
            paddingBottom: "20px"
          }}>
            {/* Company Logo */}
            <div style={{ width: "40px", height: "40px", paddingLeft: "15px", paddingRight: "20px" }}>
              <img
                src={`https://cdn.simpleicons.org/${job.company.toLowerCase()}`}
                alt={`${job.company} logo`}
                style={{ width: "100%", height: "100%", objectFit: "contain" }}
              />
            </div>

            {/* Job Details */}
            <div style={{ flex: 1 }}> {/* Allows the details to expand and fill available space */}
              <a
                href={job.url}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                //   fontSize: "16px",
                  fontWeight: "bold",
                  textDecoration: "none",
                  color: "#007bff"
                }}
              >
                {job.title}
              </a>
              <br /> {/* Line break */}
              <span style={{ fontWeight: "bold" }}>{job.company}</span>
            </div>

            {/* Location */}
            <div style={{
              width: "150px",
              textAlign: "left",
              paddingRight: "50px",
            //   paddingLeft: "20px"
            }}>
                {job.location.endsWith('ISR')
                ? job.location.split(',')[0]
                : job.location}
            </div>

            {/* Posted Date */}
            <div style={{ 
              width: "200px", 
            //   fontSize: "14px", 
              color: "#666",
              textAlign: "left",
              marginRight: "-35px"
            }}>
              {dateForm(job.posted_date)}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default JobList;