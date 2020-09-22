Sub Stockmarket():
'running the code through the entire worksheet
For each ws In Worksheets

'Inserting headers in the excel sheet
ws.Cells(1, 9).value = "Ticker"
ws.Cells(1,10).value = "Yearly Change"
ws.Cells(1,11).value = "Percent Change"
ws.Cells(1,12).value = "Total Stock Volume"

'Assigning the variables through our code
Dim i as Long
Dim ticker as String

Dim StartPrice as double
StartPrice = 0

Dim ClosePrice as double
ClosePrice = 0

Dim StockVolume as double
StockVolume = 0

'Calculating yearly change ClosePrice - StartPrice
Dim YearlyChange as double
YearlyChange = 0

Dim PercentChange as double
PercentChange = 0

'Start data at row 2 since row 1 is headers
Dim TickerRow as Long
TickerRow = 2

'Counting to the last row in sheet
Dim Lastrow as Long
LastRow = ws.Cells(Rows.Count, 1).End(xlUp).row
'-------------------------------------------------------------------------------------
    'Calculating opening price with a reference value 
    StartPrice = ws.Cells(2, 3).value

    'Writing for loop with the variables declared
    for i = 2 to LastRow

        'Being loop through ticker to find the next change in value
        If ws.Cells(i+1, 1).value <> ws.Cells(i, 1).value Then

            'Set the Ticker Name for the data
            Ticker = ws.Cells(i, 1).value

            'Calcualting Yearly Price Change amd the overall Percent Change

            ClosePrice = ws.Cells(i, 6).value
            YearlyChange = ClosePrice - StartPrice

            if StartPrice <> 0 Then 
                PercentChange = (YearlyChange/StartPrice) * 100

                'Calculating the total volume for the stock ticker

                StockVolume = StockVolume + ws.Cells(i, 7).value
        
