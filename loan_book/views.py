from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serailizer import LoanSerailizer
from .models import LoanBook
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([AllowAny])
def create_loan(request):
    serailizer = LoanSerailizer(data=request.data)
    if serailizer.is_valid(raise_exception=True):
        serailizer.save()
        return Response(serailizer.data)
    return Response(serailizer.errors)
    

@api_view(["GET"])
@permission_classes([AllowAny])
def get_loan_list(request):
    loans = LoanBook.objects.all()
    serailizer = LoanSerailizer(loans,many=True)
    return Response(serailizer.data)

@api_view(["PUT"])
@permission_classes([AllowAny])
def update_loan_view(request,pk):
    loan = LoanBook.objects.filter(pk=pk).first()

    if loan:
        serializer = LoanSerailizer(loan,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.data)
    return Response("loan not found")


@api_view(["DELETE"])
@permission_classes([AllowAny])
def delete_loan(request,pk):
    loan = LoanBook.objects.filter(pk=pk).first()
    if loan:
        loan.delete()
    return Response("Loan not found")


@api_view(["GET"])
@permission_classes([AllowAny])
def get_loan(request,pk):
    loan = LoanBook.objects.filter(pk=pk).first()
    serailizer = LoanSerailizer(loan)
    return Response(serailizer.data)





