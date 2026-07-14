function ResultBox({ result, }) {
    return (
        <div className='result-box'>
            <h3>Result</h3>
            
            {loading ? (
                <p>Loading...</p>
            ) : (
                <pre>{result}</pre>
            )}
        </div>
    );
}
export default ResultBox;