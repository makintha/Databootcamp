Sub Fizzbuzz()
    For i = 2 To 99
        If Cells(i, 1).Value Mod 3 = 0 Then
            Cells(i, 2).Value = "Fizz"
        ElseIf Cells(i, 1).Value Mod 5 = 0 Then
            Cells(i, 2).Value = "Buzz"
        ElseIf Cells(i, 1).Value Mod 3 = 0 And  Mod 5 = 0 Then
            Cells(i, 2).Value = "Fizz Buzz"
        
        End If
        
    Next i
           
End Sub