import os
import csv

election_cvs = os.path.join("Resources", "election_data.csv")


class Main:
    def election_count():
        # Variables
        total_votes = 0
        # candidates_profile = ["Charles Casper Stockham","Raymon Anthony Doane", "Diana DeGette"]
        votes_Charles = 0
        votes_Diana = 0
        votes_Raymon = 0
        vote_percent_Charles = 0
        vote_percent_Diana = 0
        vote_percent_Raymon = 0
        winner = ""

        # Read in the CSV file
        with open(election_cvs, 'r') as csvfile:
            # Crea un lector CSV
            csv_reader = csv.reader(csvfile)

            # Skip the header row
            header = next(csv_reader)

            for row in csv_reader:
                # We will extract the votes and update the value to add and have the candidates_profile
                name = row[2]

                if name == "Charles Casper Stockham":
                    votes_Charles += 1
                elif name == "Diana DeGette":
                    votes_Diana += 1
                elif name == "Raymon Anthony Doane":
                    votes_Raymon += 1

                total_votes += 1

        winner = max([(votes_Charles, "Charles Casper Stockham"),
                     (votes_Diana, "Diana DeGette"), (votes_Raymon, "Raymon Anthony Doane")])[1]
        vote_percent_Charles = (votes_Charles / total_votes) * 100
        vote_percent_Diana = (votes_Diana / total_votes) * 100
        vote_percent_Raymon = (votes_Raymon / total_votes) * 100

        # Print the analysis results

        print(f"")
        print("Election Results")
        print(f"")
        print("-------------------------")
        print(f"")
        print(f"Total: {total_votes}")
        print(f"")
        print("-------------------------")
        print(f"")
        print(
            f"Charles Casper Stockham: {vote_percent_Charles:.2f}% ({votes_Charles}) ")
        print(
            f"Diana DeGette: {vote_percent_Diana:.2f}% ({votes_Diana}) ")
        print(
            f"Raymon Anthony Doane: {vote_percent_Raymon:.2f}% ({votes_Raymon}) ")
        print(f"")
        print("-------------------------")
        print(f"")
        print(
            f"Winner: {winner}")
        print("-------------------------")
        print(f"")


if __name__ == "__main__":
    analyzer_votes = Main
    analyzer_votes.election_count()
