Sub GroupTicker()

    ' Set an initial variable for holding the brand name
    Dim Ticker As String

    ' Set an initial variable for holding the total stock per ticker
    Dim Stock_Total As Double
    Stock_Total = 0

    ' Yearly Change
    Dim YO As Double, YC As Double
    
    ' Loop worksheet
    For Each ws In Worksheets
        
        ' Last Row each Worksheet
        LastRow = ws.Cells(Rows.Count, "A").End(xlUp).Row
        
        ' Header
        ws.Cells(1, 9).Value = "Ticker"
        ws.Cells(1, 10).Value = "Yearly_Change"
        ws.Cells(1, 11).Value = "Pct Change"
        ws.Cells(1, 12).Value = "Volume"
        
        'ticker row counter
        Ticker = 1
        
        ' Loop row for each workshet
        For i = 2 To LastRow
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                ' ticker
                Ticker = Ticker + 1
                ws.Cells(Ticker, 9).Value = ws.Cells(i, 1)
            
                ' Add to the Brand Total
                Stock_Total = Stock_Total + ws.Cells(i, 7).Value
                ws.Cells(Ticker, 12).Value = Stock_Total
                
                ' Reset Stock Total
                Stock_Total = 0
                
                If i = LastRow Then
                    Exit For
                    
                Else
                    
                    ' Mark close value on last date for earlier ticker and Mark Open value for first date for new ticker
                    YC = ws.Cells(i, 6).Value
                    ' fill in yr change and pct change
                    If Ticker = 2 Then
                        ' fill in first ticker
                        ws.Cells(Ticker, 10).Value = YC - ws.Cells(2, 3).Value
                        ws.Cells(Ticker, 11).Value = (ws.Cells(Ticker, 10).Value) / ws.Cells(2, 3).Value
                
                    ElseIf Ticker > 2 Then
                        ws.Cells(Ticker, 10).Value = YO_new - Yr_1
                        ws.Cells(Ticker, 11).Value = (ws.Cells(Ticker, 10).Value) / Yr_0

            End If
                    ws.Cells(i + 1, 3).Value = YO_new

                End If

            End If
            
            YO = YO_new
            

            
            
            
            Stock_Total = Stock_Total + ws.Cells(i, 7).Value
            
        Next i
    
    Next ws
    


End Sub
