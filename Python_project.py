# importing the required module 
'''Problem Statement: Develop a Python script to visualize and analyze diverse mathematical functions using Matplotlib 
            and NumPy libraries. The script should allow users to explore and comprehend the behaviour of linear, 
            quadratic, sine, exponential, trigonometric, and inverse trigonometric functions. Additionally, the 
            script should provide functionality to determine and display Euler paths or circuits for user-defined 
            graphs using NetworkX.
   Domain: Mathematics,Visualization

   *Team Members*
   Kishan Dinesh Mali (A_36)
   Shrikrushna Sanjay Jadhav (A_27)
   Harish Dattatray Lukare (A_35)

'''
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


# x axis values 
x = np.linspace(-5, 5, 100)  # Generating 100 points from -5 to 5
def Linear():
# Example 1: Plotting a linear function
    y_linear = 2 * x + 3
    plt.figure()
    plt.plot(x, y_linear, label='Linear Function')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Linear Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()
    plt.show()

def Quadratic():
    # Example 2: Plotting a quadratic function
    y_quadratic =  x**2 - 2*x + 1
    plt.figure()
    plt.plot(x, y_quadratic, label='Quadratic Function')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Quadratic Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()
    plt.show()


def Sine():
# Example 3: Plotting a sine function
    y_sine = np.sin(x)
    plt.figure()
    plt.plot(x, y_sine, label='Sine Function')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Sine Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()
    plt.show()


def Exponential():
# Example 4: Plotting an exponential function
    y_exponential = np.exp(x)
    plt.figure()
    plt.plot(x, y_exponential, label='Exponential Function')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Exponential Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()
    plt.show()
    

def Trignometric1():
# x axis values 
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)  # Generating 1000 points from -2*pi to 2*pi

# Trigonometric Functions
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)

# Inverse Trigonometric Functions
    y_arcsin = np.arcsin(x)
    y_arccos = np.arccos(x)
    y_arctan = np.arctan(x)

# Plotting Trigonometric Functions
    plt.figure(figsize=(12, 8))

# Sine Function
    plt.subplot(2, 3, 1)
    plt.plot(x, y_sin, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sine Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

# Cosine Function
    plt.subplot(2, 3, 2)
    plt.plot(x, y_cos, label='cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cosine Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

# Tangent Function
    plt.subplot(2, 3, 3)
    plt.plot(x, y_tan, label='tan(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Tangent Function')
    plt.ylim(-5, 5)  # Limit y-axis to show tan(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

# Plotting Inverse Trigonometric Functions
# Note: Restricting the domain for arcsin and arccos to [-1, 1] for meaningful plots
    plt.subplot(2, 3, 4)
    plt.plot(x, y_arcsin, label='arcsin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Arcsine Function')
    plt.ylim(-1.5*np.pi, 1.5*np.pi)  # Limit y-axis to show arcsin(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.subplot(2, 3, 5)
    plt.plot(x, y_arccos, label='arccos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Arccosine Function')
    plt.ylim(0, np.pi)  # Limit y-axis to show arccos(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.subplot(2, 3, 6)
    plt.plot(x, y_arctan, label='arctan(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Arctangent Function')
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.tight_layout()
    plt.show()

def  Trignometric2():
# x axis values 
    x = np.linspace(-2*np.pi, 2*np.pi, 1000)  # Generating 1000 points from -2*pi to 2*pi

# Trigonometric Functions
    y_cot = 1/np.tan(x)
    y_cosec = 1/np.sin(x)
    y_sec = 1/np.cos(x)

# Inverse Trigonometric Functions
    y_arccot = np.arctan(1/x)
    y_arccosec = np.arcsin(1/x)
    y_arcsec = np.arccos(1/x)

# Plotting Trigonometric Functions
    plt.figure(figsize=(12, 8))

# Cotangent Function
    plt.subplot(2, 3, 1)
    plt.plot(x, y_cot, label='cot(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cotangent Function')
    plt.ylim(-5, 5)  # Limit y-axis to show cot(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

# Cosecant Function
    plt.subplot(2, 3, 2)
    plt.plot(x, y_cosec, label='cosec(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cosecant Function')
    plt.ylim(-5, 5)  # Limit y-axis to show cosec(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

# Secant Function
    plt.subplot(2, 3, 3)
    plt.plot(x, y_sec, label='sec(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Secant Function')
    plt.ylim(-5, 5)  # Limit y-axis to show sec(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

# Plotting Inverse Trigonometric Functions
# Note: Restricting the domain for arccot, arccosec, and arcsec for meaningful plots
    plt.subplot(2, 3, 4)
    plt.plot(x, y_arccot, label='arccot(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Arccotangent Function')
    plt.ylim(-1.5*np.pi, 1.5*np.pi)  # Limit y-axis to show arccot(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.subplot(2, 3, 5)
    plt.plot(x, y_arccosec, label='arccosec(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Arccosecant Function')
    plt.ylim(-1.5*np.pi, 1.5*np.pi)  # Limit y-axis to show arccosec(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.subplot(2, 3, 6)
    plt.plot(x, y_arcsec, label='arcsec(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Arcsecant Function')
    plt.ylim(0, np.pi)  # Limit y-axis to show arcsec(x) behavior
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.legend()

    plt.tight_layout()
    plt.show()

def EularPathAndCircuit():
    #edges_str = input("Enter the edges of the graph (format: '1-2 2-3 3-4 4-1 1-3'): ")
    #edges_list = [tuple(map(int, edge.split('-'))) for edge in edges_str.split()]
    edges_list = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
    # Create a graph from user input
    G = nx.Graph()
    G.add_edges_from(edges_list)
    # Find Euler path or circuit
    euler_path, euler_circuit = find_euler_path_or_circuit(G)
    # Visualize the graph and Euler path or circuit
    visualize_euler_graph(G, euler_path, euler_circuit)

# Euler path and Euler circuit

def visualize_euler_graph(graph, euler_path=None, euler_circuit=None):
    pos = nx.spring_layout(graph)  # Layout for better visualization
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold')

    if euler_path:
        nx.draw_networkx_edges(graph, pos, edgelist=euler_path, edge_color='red', width=2, arrowsize=10, connectionstyle='arc3,rad=0.1')
    elif euler_circuit:
        nx.draw_networkx_edges(graph, pos, edgelist=euler_circuit, edge_color='green', width=2, arrowsize=10, connectionstyle='arc3,rad=0.1')

    plt.title("Euler Path and Circuit Visualization")
    plt.show()

def find_euler_path_or_circuit(graph):
    # Check if the graph has an Euler path or circuit
    if not nx.is_eulerian(graph):
        print("The graph does not have an Euler path or circuit.")
        return None, None

    # Find an Euler path (if it exists)
    euler_path = list(nx.eulerian_path(graph))

    # Find an Euler circuit (if it exists)
    euler_circuit = list(nx.eulerian_circuit(graph))

    return euler_path, euler_circuit

# Get user input for graph edges

def Cipher_Function() :
    #print("Hello World")

    def encrypt_alpha(message, key):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                offset = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - offset + key) % 26 + offset)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt_alpha(encrypted_message, key):
        return encrypt_alpha(encrypted_message, -key)

# Get user input
    input_type = input("Enter 'alpha' for alphabets: ")

    if input_type == 'alpha':
        message = input("Enter the message: ")
        choice = input("Enter 'encrypt' or 'decrypt': ")

        if choice == 'encrypt':
            key = int(input("Enter the key: "))
            result = encrypt_alpha(message, key)  # Only call the alphabetic encryption function

        elif choice == 'decrypt':
            key = int(input("Enter the key: "))
            result = decrypt_alpha(message, key)  # Only call the alphabetic decryption function

        else:
            result = "Invalid choice."

    else:
        result = "Invalid input type choice."

# Display result
    print(f"Result: {result}")
 



temp=1
while(temp==1):
    print("CHHOSE YOUR GRAPH")
    print("1) LINEAR FUNCTION ")
    print("2) QUADRATIC FUNCTION ")
    print("3) SINE FUNCTION ")
    print("4) EXPONENTIAL FUNCTION ")
    print("5) TRIGONOMETRIC 1 FUNCTION ")
    print("6) TRIGONOMETRIC 2 FUNCTION ")
    print("7) EULER PATH OR CIRCUIT ")
    print("8) Cipher Function ")
    print("9) EXITING")
    choice = int(input())
    match choice:
        case 1:
            Linear()
        case 2:
            Quadratic()
        case 3:
            Sine()
        case 4:
            Exponential()
        case 5:
            Trignometric1()
        case 6:
            Trignometric2()    
        case 7:
            EularPathAndCircuit()
        case 8:
            Cipher_Function()
        case 9:
            temp = 0


'''
-----------------------------Code Summary and Explanation----------------------------------
***Libraries Used:***
Matplotlib: Used for plotting various mathematical functions.
Numpy: Employed for numerical operations and array manipulation.
NetworkX: Utilized for graph-related operations, specifically in Euler path/circuit visualization.

***Functions:***
Linear():
Plots a linear function of the form y = 2x + 3.
We can give chage the expression (y = 2x + 3)
similarly we can change for quadratic (also for ILATE Functions)

Quadratic():
Plots a quadratic function of the form y = x^2 - 2x + 1.

Sine():
Plots a sine function.

Exponential():
Plots an exponential function using numpy's exponential function.

Trignometric1():
Plots common trigonometric functions (sin, cos, tan) and their inverses (arcsin, arccos, arctan).

Trignometric2():
Extends trigonometric plots to include cotangent, cosecant, secant, and their inverses.

EularPathAndCircuit():
Creates a graph using NetworkX and visualizes Euler paths or circuits if they exist.

Cipher_Function():
Implements a basic Caesar cipher for encrypting and decrypting alphabetic messages.

***User Interaction:***
Users are presented with a menu to choose mathematical functions or cryptographic operations.
The program loops until the user selects the exit option.
***Additional Information:***
Euler functions employ graph theory concepts, checking for Eulerian paths or circuits in a graph using NetworkX.
The Cipher_Function enables users to encrypt or decrypt messages using a Caesar cipher with a specified key.
'''