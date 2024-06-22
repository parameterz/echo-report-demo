async function submitForm(event) {
    event.preventDefault();
    const eWave = document.getElementById('eWave').value;
    const aWave = document.getElementById('aWave').value;
    const ePrime = document.getElementById('ePrime').value;

    const response = await fetch('https://5zbjy0f4se.execute-api.us-east-2.amazonaws.com/test/report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ eWave, aWave, ePrime }),
    });

    const result = await response.json();
    document.getElementById('report').innerText = result.report;
}
