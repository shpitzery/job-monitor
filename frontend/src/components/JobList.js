function JobList({ jobs }) {
  const dateForm = (postedDate) => {
    // First, check if it's a relative date format
    if (postedDate.includes('Days Ago')) {
        return postedDate;
    }

    // Handle regular date format
    const dateStr = postedDate.toLowerCase().startsWith('posted') 
        ? postedDate.slice(7).trim() 
        : postedDate.trim();

    // Try to parse the date
    const date = new Date(dateStr);

    // Check if the date is valid
    if (isNaN(date.getTime())) {
        console.log('Invalid date:', dateStr);
        return 'Invalid Date'; // Or handle error as needed
    }

    // Format the valid date
    const month = date.toLocaleString('en-US', { month: 'short' });
    const day = date.getDate();
    const year = date.getFullYear();
    return `Posted ${month} ${day}, ${year}`;
};

  return (
    <div style={{ width: "80%", maxWidth: "1200px", margin: "auto" }}>
      <h2 style={{ textAlign: "center", marginBottom: "20px" }}>Featured Jobs</h2>
      <div style={{
        border: "1px solid #ddd",
        borderRadius: "10px",
        overflow: "hidden", // Ensures child elements don't cross the border
      }}>
        {jobs.map((job, index) => (
          <div key={index} style={{
            display: "flex",
            alignItems: "center",
            padding: "20px",
            borderBottom: "1px solid #ddd",
            backgroundColor: index % 2 === 0 ? "#fff" : "#f9f9f9",
            fontSize: "16px",
            textWrap: "wrap",
          }}>
            {/* Company Logo */}
            <div style={{ width: "40px", height: "40px", padding: "0 20px" }}>
              <img
                src={`https://cdn.simpleicons.org/${job.company.toLowerCase()}`}
                alt={`${job.company} logo`}
                style={{ width: "100%", height: "100%", objectFit: "contain" }}
              />
            </div>

            {/* Job Details */}
            <div style={{ flex: "1 1 auto", minWidth: "0" }}> {/* Allows the details to expand and fill available space */}
              <a
                href={job.url}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  fontWeight: "bold",
                  textDecoration: "none",
                  color: "#007bff",

                }}
              >
                {job.title}
              </a>
              <br /> {/* Line break */}
              <span style={{ fontWeight: "bold" }}>{job.company}</span>
            </div>

            {/* Location */}
            <div style={{
              flex: "0 1 150px",
              textAlign: "left",
              padding: "0 35px",
            }}>
              {(() => {
                const loc = job.location;
                
                // If location ends with ISR, remove ISR and any "Israel," prefix
                if (loc.endsWith('ISR')) {
                  return loc.split(',')[0].replace(/israel,\s*/i, "");
                }
        
                // If location contains "Israel," anywhere, remove it
                if (loc.match(/israel,\s*/i)) {
                  return loc.replace(/israel,\s*/i, "");
                }
        
        
                // If none of the above conditions match, return the original location
                return loc;
              })()}
            </div>

            {/* Posted Date */}
            <div style={{ 
              flex: "0 1 200px",
              color: "#666",
              textAlign: "left",
              // padding: "0 20px",
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