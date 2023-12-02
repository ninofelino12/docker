import csv

def export_data_to_file():
    # Use Odoo ORM methods to query data
    records = env['your.model'].search([])

    # Prepare data for export
    data_to_export = []
    for record in records:
        data_to_export.append({
            'field1': record.field1,
            'field2': record.field2,
            # Add more fields as needed
        })

    # Write data to a CSV file
    with open('/path/to/exported_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['field1', 'field2']  # Add field names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data rows
        for row in data_to_export:
            writer.writerow(row)
