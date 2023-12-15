import pyrddlgym

def main():
    
    env = pyrddlgym.make("grid_world_instance.rddl")

    state, done = env.reset(), False

    while not done:
        # Choose an action (randomly for this example)
        action = env.action_space.sample()
        # Step the environment forward
        next_state, reward, done, _ = env.step(action)
        # Update the current state
        state = next_state
    # Close the environment
    env.close()

if __name__ == "__main__":
    main()
