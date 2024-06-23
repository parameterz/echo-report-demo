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

    const data = await response.json();
    const report = `
        Diastolic Function Report:

        E Wave Velocity: ${data.eWave.toFixed(2)} cm/s
        A Wave Velocity: ${data.aWave.toFixed(2)} cm/s
        E' Velocity: ${data.ePrime.toFixed(2)} cm/s
        E/A Ratio: ${data.eaRatio.toFixed(1)}
        E/e\' Ratio: ${data.eePrimeRatio.toFixed(1)}

        Conclusion: ${data.conclusion}
    `;
    document.getElementById('report').innerText = report;
}
