Sub Stockmarket():
'running the code through the entire worksheet
For Each ws In Worksheets

'Inserting headers in the excel sheet
ws.Cells(1, 9).Value = "Ticker"
ws.Cells(1, 10).Value = "Yearly Change"
ws.Cells(1, 11).Value = "Percent Change"
ws.Cells(1, 12).Value = "Total Stock Volume"

'Assigning the variables through our code
Dim i As Long
Dim ticker As String

Dim StartPrice As Double
StartPrice = 0

Dim ClosePrice As Double
ClosePrice = 0

Dim StockVolume As Double
StockVolume = 0

'Calculating yearly change ClosePrice - StartPrice
Dim YearlyChange As Double
YearlyChange = 0

Dim PercentChange As Double
PercentChange = 0

'Start data at row 2 since row 1 is headers
Dim TickerRow As Long
TickerRow = 2

'Counting to the last row in sheet
Dim Lastrow As Long
Lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
'-------------------------------------------------------------------------------------
    'Calculating opening price with a reference value
    StartPrice = ws.Cells(2, 3).Value

    'Writing for loop with the variables declared
    For i = 2 To Lastrow

        'Being loop through ticker to find the next change in value
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

            'Set the Ticker Name for the data
            ticker = ws.Cells(i, 1).Value

            'Calcualting Yearly Price Change amd the overall Percent Change

            ClosePrice = ws.Cells(i, 6).Value
            YearlyChange = ClosePrice - StartPrice

            If StartPrice <> 0 Then
                PercentChange = (YearlyChange / StartPrice) * 100

                'Calculating the total volume for the stock ticker

                StockVolume = StockVolume + ws.Cells(i, 7).Value
            End If
    '-------------------------------------------------------------------------------------------------
    'Printing ranges into the cells
                'Printing Ticker name
                ws.Range("I" & TickerRow).Value = ticker

                'Print Yearly Change
                ws.Range("J" & TickerRow).Value = YearlyChange

                'Print the Percent Change
                ws.Range("K" & TickerRow).Value = (Str(PercentChange) & "%")

                'Print Stock Volume
                ws.Range("L" & TickerRow).Value = StockVolume

                'Print next Ticker Row in Table
                TickerRow = TickerRow + 1

                'Reset the values for the next ticker symbols
                YearlyChange = 0
                StartPrice = ws.Cells(i + 1, 3).Value
                ClosePrice = 0
                PercentChange = 0
                StockVolume = 0
            Else
                StockVolume = StockVolume + ws.Cells(i, 7).Value
        End If
    Next i
Next ws
End Sub

