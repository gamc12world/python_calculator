import rich
def _calculator(operator:str,x1:list):
    add=0
    mul=1
    final=0
    div=1
    for i in x1:
       match operator:
            case '+':
             add=i+add
            case '-':
               final=i-final
            case "*":
               mul=mul*i
            case "/":
               div=i/div
            case _:
             print("nothing matched up")
    match operator:
       case "+":
          rich.get_console().print(f"[bold underline green]{add}[/bold underline green]")
       case "-":
          rich.get_console().print(f"[bold white]{final}[/bold white]")
       case "*":
          rich.get_console().print(f"[bold blue]{mul}[/bold blue]")
       case '/':
          rich.get_console().print(f"[bold purple]{div}[/bold purple]")    
    pass
x1=[]
ask_operation=input("enter the operation")
x13=rich.get_console()
while True:
   asked_no=rich.get_console().input("[underline red]enter the no.[/underline red]")
   if asked_no=="done":
      break
   else:
      x1.append(int(asked_no))
   pass
_calculator(ask_operation,x1)
