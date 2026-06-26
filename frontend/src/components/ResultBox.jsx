function ResultBox({ result }) {
    return (
        <div className='result-box'>
            <h3>Result</h3>
            
            if(loading){
                <p>Loading...</p>
            }
            else{
                <p>{result}</p>
            }
        </div>
    );
}
export default ResultBox;