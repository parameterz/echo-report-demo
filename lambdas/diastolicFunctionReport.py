import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        e_wave = float(body['eWave'])
        a_wave = float(body['aWave'])
        e_prime = float(body['ePrime'])

        # Calculate ratios
        ea_ratio = e_wave / a_wave
        eeprime_ratio = e_wave / e_prime

        # Sample evaluation logic (to be replaced with actual algorithm)
        if eeprime_ratio > 14:
            conclusion = "Impaired diastolic function with elevated filling pressures."
        elif eeprime_ratio > 10:
            conclusion = f"Gray area; E/e' ratio is greater than 10 ({eeprime_ratio:.1f})."
        else:
            conclusion = "Normal diastolic function."

        # Construct the response data
        response_data = {
            'eWave': e_wave,
            'aWave': a_wave,
            'ePrime': e_prime,
            'eaRatio': ea_ratio,
            'eePrimeRatio': eeprime_ratio,
            'conclusion': conclusion
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_data),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }
        }

    except Exception as e:
        print("Error: ", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }
        }
