import os


def main():
  nombre = os.getenv("USERNAME")
  print(f"¡hola, {nombre} desde GitHub!")


if __name__ == "__main__":
  main()
