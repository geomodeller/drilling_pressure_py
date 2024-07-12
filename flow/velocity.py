

def velocity(q, openhole, pipe_OD):
    vel = q / 2.448 / (openhole**2 - pipe_OD**2)
    return vel
