function JobList({ jobs }) {
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
                        padding: "15px",
                        borderBottom: "1px solid #ddd",
                        backgroundColor: index % 2 === 0 ? "#fff" : "#f9f9f9",
                    }}>
                        {/* Display Apple Icon only for Apple jobs */}
                        <div style={{ width: "40px", height: "40px", marginRight: "15px" }}>
                            {/* {job.company.toLowerCase() === "apple" ? (
                                <AppleIcon width={40} height={40} color="black" />
                            ) : ( */}
                                <img
                                    src={`https://cdn.simpleicons.org/${job.company.toLowerCase()}`}
                                    alt={`${job.company} logo`}
                                    style={{ width: "100%", height: "100%", objectFit: "contain" }}
                                />
                            {/* )} */}
                        </div>

                        {/* Job Details */}
                        <div style={{ flex: 1 }}>
                            <a
                                href={job.url}
                                target="_blank"
                                rel="noopener noreferrer"
                                style={{
                                    fontSize: "16px",
                                    fontWeight: "bold",
                                    textDecoration: "none",
                                    color: "#007bff"
                                }}
                            >
                                {job.title}
                            </a>
                            <br />
                            <span style={{ fontWeight: "bold" }}>{job.company}</span>
                        </div>

                        {/* Location */}
                        <div style={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "center",
                            textAlign: "center",
                            width: "200px",
                            height: "40px",
                            marginRight: "25px",
                            }}>
                            <span>{job.location}</span>
                        </div>

                        {/* Job Type Badge */}

                        {/* {job.type && (
                            <div style={{
                                backgroundColor: "#007bff",
                                color: "white",
                                padding: "5px 10px",
                                borderRadius: "5px",
                                fontSize: "12px",
                                fontWeight: "bold",
                                textAlign: "center",
                                minWidth: "80px"
                            }}>
                                {job.type.toUpperCase()}
                            </div>
                        )} */}

                        {/* Date Posted */}
                        <div style={{ fontSize: "12px", color: "#666", marginLeft: "15px" }}>
                        {job.posted_date.toLowerCase().includes("posted") ? job.posted_date : `Posted ${job.posted_date}`}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default JobList;