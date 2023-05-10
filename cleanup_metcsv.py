import csv

with open('object_info.csv', 'r', encoding='utf8') as file:
    reader = csv.DictReader(file)

    rows = []

    for row in reader:
        # Clean up Artist Suffix field, if applicable
        row['Artist Suffix'] = row['Artist Suffix'].replace(",", "").strip()
        
        # If the Classification field is blank, copy over the info from the "Medium Field"
        if not row['Classification']:
            row['Classification'] = row['Medium']
        
        # Calculate date average between the Earliest and Latest Date fields
        earliest_date = row['Earliest Date']
        latest_date = row['Latest Date']
        if earliest_date and latest_date:
            date_average = str((int(earliest_date) + int(latest_date)) / 2)
        else:
            date_average = ''

        # Add Date Average info to the row
        row['Date Average'] = date_average

        
        rows.append(row)

    # Now we're going to write it all into a new, cleaned file
    with open('met_objects_cleaned.csv', 'w', encoding='utf8', newline='') as output_file:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(output_file, fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    print('Done!')