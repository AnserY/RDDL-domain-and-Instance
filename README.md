# RDDL-domain-and-Instance
RDDL (Relational Dynamic Influence Diagram Language) is used for specifying domains and instances in decision-theoretic planning problems, especially those with complex, structured, and dynamic environments. This repository provide an example of a simple RDDL domain and instance where we consider a simple grid world where an agent moves to collect rewards. Also, we use pyRDDLgym in order to create the environement and we implement a RL agent. 

# RDDL Domain File
The domain file describes the types, predicates, actions, and dynamics of the environment. 
### Explanation 
- type : we define the type 'position' representing grid position.
- pvariables: Defines state and action variables :
    - agent_at : fluent state variable indicating the agent's position.
    - reward : fluent state variable indicating whether a reward is present at a certain position.
    - move : action variable representing possible movements.
- cpfs :
    - agent_at : specifies how the agent's position changes based on the action taken.
    - reward' : specifies how the reward presence changes. 

- reward: Specifies the reward function. Here, it's based on the agent's position and reward presence.

# RDDL Instance File
The instance file specifies the particular scenario within the domain.
### Explanation
- non-fluents nf_grid_world: Defines non-fluent data specific to this instance :
    - Specifies the domain it belongs to and defines objects for the position type.
    - Initial settings for the reward at each position.
- init-state: Defines the initial state of the environment. Here, the agent starts at pos1.
- max-nondef-actions: The maximum number of non-default actions the agent can take per step.
- horizon: The length of the decision problem, in time steps.
- discount: The discount factor for future rewards, affecting how future rewards are valued relative to immediate rewards.  
