function JobList({ jobs }) {
    return (
        <ul>
            {jobs.map((job, index) => (
                <li key={index}>
                    <a href={job.url} target="_blank" rel="noopener noreferrer">
                        {job.title} ({job.posted_date})
                    </a>
                </li>
            ))}
        </ul>
    );
}

export default JobList;