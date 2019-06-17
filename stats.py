"""Executes Git stats calls to determine user metrics."""
from git import Git


class UserStats:
    """Git stats calculated for specified users."""

    def get_net_lines(self, user: str, repo: str) -> int:
        """gets net add by specified user for file in repo with 'master' in title."""
        g = Git(repo)
        loginfo = g.log(f'--author={user}', '--pretty=tformat:', '--numstat')
        parsed_numbers = [int(loginfo) for loginfo in loginfo.split() if loginfo.isdigit()]

        count = 0
        net = 0
        for num in parsed_numbers:
            if count % 2 == 0:
                net += num
            else:
                net -= num
            count += 1
        net_lines = net

        return net_lines


if __name__ == '__main__':
    stats = UserStats()
    net_lines = stats.get_net_lines('markdavidmc0', '/Users/markmc/Repos/colab-tester')
    print(net_lines)
