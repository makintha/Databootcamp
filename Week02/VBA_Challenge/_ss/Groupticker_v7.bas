Attribute VB_Name = "Module1"
Attribute VB_Name = "Module1"
Sub GroupTicker()

    ' Set an initial variable for holding the brand name
    Dim Ticker As String

    ' Set an initial variable for holding the total stock per ticker
    Dim Stock_Total As Double
    Stock_Total = 0

    ' Yearly Change
    Dim Opening As Double, Closing As Double, Index_Opening As Integer, Index_Closing As Integer
    
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
                in_closing = ws.Cells(j, 13).Value
                Closing = ws.Cells(in_closing, 6).Value
            Else
                in_opening = ws.Cells(j - 1, 13).Value
                Opening = ws.Cells(in_opening + 1, 3).Value
                in_closing = ws.Cells(j, 13).Value
                Closing = ws.Cells(in_closing, 6).Value
            End If
            
            ' Yearly Change
            If Opening = 0 And Closing = 0 Then
                ws.Cells(j, 10).Value = 0
                ws.Cells(j, 11).Value = 0
                MsgBox ("NOTICE:" & vbCrLf & "This Worksheet has incomplete dataset" & vbCrLf & "The Problem data is at Ticker" & ws.Cells(j, 9))
            Else
                ws.Cells(j, 10).Value = Closing - Opening
                ws.Cells(j, 11).Value = ws.Cells(j, 10).Value / Opening

            End If
            
                        
            ' Set the Cell Colors to Red
            If ws.Cells(j, 11) < 0 Then
                ws.Cells(j, 11).Interior.ColorIndex = 3
            Else
                ws.Cells(j, 11).Interior.ColorIndex = 4
            End If
            
        Next j
    
        ' Tidy up
        ws.Range("M1:M" & NTicker) = ""
        ' Format column to percentace
        ws.Range("K2:K" & NTicker).NumberFormat = "0.00%"
        ws.Range("Q2:Q3").NumberFormat = "0.00%"
    
    
        ' Label
        ws.Cells(2, 15).Value = "Greatest % Increase"
        ws.Cells(3, 15).Value = "Greatest % Decrease"
        ws.Cells(4, 15).Value = "Greatest Total Volume"
        ws.Cells(1, 16).Value = "Ticker"
        ws.Cells(1, 17).Value = "Value"
    
        'Find min/max value
        Minimum = Application.WorksheetFunction.Min(ws.Range("K2:K" & NTicker))
        ws.Cells(3, 17).Value = Minimum
    
        Maximum = Application.WorksheetFunction.Max(ws.Range("K2:K" & NTicker))
        ws.Cells(2, 17).Value = Maximum
    
        Max_Vol = Application.WorksheetFunction.Max(ws.Range("L2:L" & NTicker))
        ws.Cells(4, 17).Value = Max_Vol
    
        For i = 2 To NTicker
            If ws.Range("Q2").Value = ws.Cells(i, 11).Value Then
                ws.Cells(2, 16).Value = ws.Cells(i, 9).Value
            End If
            If ws.Range("Q3").Value = ws.Cells(i, 11).Value Then
                ws.Cells(3, 16).Value = ws.Cells(i, 9).Value
            End If
            If ws.Range("Q4").Value = ws.Cells(i, 12).Value Then
                ws.Cells(4, 16).Value = ws.Cells(i, 9).Value
            End If
        Next i
    
    Next ws
    


End Sub


