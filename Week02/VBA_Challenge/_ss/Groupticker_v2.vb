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
        ws.Cells(1, 13).Value = "Border"
        
        'ticker row counter
        Ticker = 1
        
        ' Loop row for each workshet
        For i = 2 To LastRow
            
            Stock_Total = Stock_Total + ws.Cells(i, 7).Value

            
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                ' Mark Border
                ' ticker
                Ticker = Ticker + 1
                ws.Cells(Ticker, 9).Value = ws.Cells(i, 1)
                ws.Cells(Ticker, 13).Value = i

            
                ' Add to the Brand Total
'                Stock_Total = Stock_Total + ws.Cells(i, 7).Value
                ws.Cells(Ticker, 12).Value = Stock_Total
                
                ' Reset Stock Total
                Stock_Total = 0
                
            End If
            
        Next i
        
        ' Number of Ticker
        NTicker = ws.Cells(Rows.Count, "M").End(xlUp).Row
        For j = 2 To NTicker
            If j = 2 Then
                Opening = ws.Cells(j, 3).Value
                Index_Closing = ws.Cells(j, 13).Value
                Closing = ws.Cells(Index_Closing, 6).Value
            ElseIf j > 2 Then
                Index_Opening = ws.Cells(j - 1, 13).Value
                Opening = ws.Cells(Index_Opening + 1, 3).Value
                Index_Closing = ws.Cells(j, 13).Value
                Closing = ws.Cells(Index_Closing, 6).Value
            End If
            
            ' Yearly Change
            ws.Cells(j, 10).Value = Closing - Opening
            ws.Cells(j, 11).Value = ws.Cells(j, 10).Value / Opening
            
        Next j
    
    Next ws
    


End Sub

