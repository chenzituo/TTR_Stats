# Ticket To Ride Network Analysis Design Principles

## Degree distribution and edge weights
- Node degree (city connections) ranges 1–7.
- About 15 cities have degree 4 and 14 cities have degree 3.
- One city has degree 7; two cities have degree 6.
- Edge weight corresponds to track length.
- Edge weight distribution: ~33 edges with weight 2, 26 with weight 4, 25 with weight 3, 2 with weight 6, and 1 with weight 8.

## Player count and blocking difficulty
- Difficulty rises with more players.
- 3-player game: ~10% of cities have degree < 3, blocking is difficult.
- 5-player game: ~72% of cities have degree < 5, blocking is easier.

## Destination card points distribution
- Few long routes: ~3 cards at 21 points and ~3 cards at 20 points.
- Many short routes: ~13 cards at 8 points.

## Network properties and strategy
- Radius: minimum edges from most central node to all others.
- Diameter: minimum edges connecting the two farthest nodes.
- Eccentricity: maximum distance from a node to all others.
- Center: nodes whose eccentricity equals the radius.
- Periphery: nodes whose eccentricity equals the diameter.

Observed values:
- Radius = 5, Diameter = 9.
- Center cities: Berlin, Venezia, Munchen.
- Periphery cities: Lisboa, Cadiz, Edinburgh, Erzurum, Sochi, Rostov, Moskva.

Strategy notes:
- Start near low eccentricity cities (Berlin, Venezia, Munchen) for flexible expansion.
- Favor destination cards including periphery cities to help build long routes.
- Consider routes among periphery cities with length equal to the diameter.

## City importance metrics
- Degree centrality: fraction of nodes connected to a node.
- Betweenness centrality: fraction of all-pairs shortest paths passing through a node.
- Closeness centrality: reciprocal of sum of shortest path distances from a node to all others.
- Clustering coefficient: ratio of neighborhood connections vs. fully connected neighborhood.
- Connectivity: minimum nodes to remove to block all paths to a node.

Observations:
- High degree centrality: Paris, Kyiv, Frankfurt.
- Low degree centrality: Edinburgh, Cadiz, Lisboa, Kobenhavn.
- High betweenness: Frankfurt, Wien, Budapest.
- Low betweenness: Brest, Palermo, Cadiz.
- High closeness: Wien, Munchen, Budapest.
- Low closeness: Cadiz, Lisboa, Edinburgh.
- Strong neighborhood clustering: Lisboa, Cadiz, Sochi, Barcelona, Brest.
- Weak neighborhood clustering: Edinburgh, Moskva, Stockholm, Kharkov, Kobenhavn, London.

## Node removal impacts (city importance)
- Removing London makes Edinburgh unreachable.
- Removing Madrid makes Lisboa and Cadiz unreachable.
- Removing Essen increases average route cost by +8.24%.
- Removing Marsielle reduces average connectivity by -10.35%.

## Edge importance
- High edge betweenness: Budapest-Wien, Zagrab-Vienna, Wien-Munchen.
- Lower edge betweenness: Rome-Venezia, Barcelona-Marsielle.
- Removing London-Edinburgh disconnects Edinburgh.
- Removing Kobenhavn-Essen increases average shortest path cost by 7.34%.
- Removing Rostov-Kharkov drops average connectivity by 8.47%.
- Removing Lisboa-Cadiz, Cadiz-Madrid, Lisboa-Madrid sharply drops average clustering.
- Efficiency drop of 2.81% when London-Edinburgh is removed.

## Destination card profitability
- Long routes (>=20 points) yield ~50–54 final points with shortest paths, using ~20–21 locomotives.
- Lisboa-Danzig (20) can yield 50 points vs Edinburgh-Athina (21) yielding 48.
- Most profitable short route: Palermo-Constantinople (8 locomotives for 25 points).
- Edge connectivity of destination routes:
  - Berlin-Bucuresti is most robust (edge connectivity 5).
  - Edinburgh-Athina, Kobenhavn-Erzurum, Cadiz-Stockholm are more vulnerable.

## Alternate scoring strategies
- Shortest path minimizes locomotives, not always max points.
- Consider alternate paths up to 2 segments longer than shortest path to improve returns.
- Example: Palermo-Moskva has multiple near-shortest alternatives with different tradeoffs.

## Blocking strategies
- Minimum edge cut identifies critical edges for blocking a route.
- Berlin-Bucuresti and Paris-Wien are most robust (5 edges to block).
- Edinburgh-Athina is most vulnerable (1 edge to block).

## Practical takeaways
- Use central cities early for flexibility.
- Target periphery cities for longest route potential.
- Prioritize high-betweenness segments if they align with your plan.
- Watch for fragile cities with weak neighborhoods to avoid getting blocked.
