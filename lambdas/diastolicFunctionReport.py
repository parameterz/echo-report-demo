import json

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        e_wave = float(body['eWave'])
        a_wave = float(body['aWave'])
        e_prime = float(body['ePrime'])
        
        # Example calculation logic
        report = f"Diastolic Function Report:\n\n"
        report += f"E Wave Velocity: {e_wave} cm/s\n"
        report += f"A Wave Velocity: {a_wave} cm/s\n"
        report += f"E' Velocity: {e_prime} cm/s\n\n"

        # Sample evaluation logic (to be replaced with actual algorithm)
        if e_wave / e_prime > 14:
            report += "Conclusion: Impaired diastolic function with elevated filling pressures."
        else:
            report += "Conclusion: Normal diastolic function."

        return {
            'statusCode': 200,
            'body': json.dumps({'report': report}),
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
