# The wrapper for calling the transform module and function
import transform as tr


if __name__ == "__main__":
    r_in = 5.0
    print("Calling the function with r={}".format(r_in))
    r_out = tr.area_circ(r_in)
