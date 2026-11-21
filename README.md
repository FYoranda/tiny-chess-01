# tiny-chess-01 entry

A 0x88-board alpha-beta chess engine in pure-stdlib Python, UCI protocol
(`uci` / `isready` / `position startpos [moves ...]` / `go` / `quit`).
Fixed depth 3 + capture quiescence, material-only evaluation, perft-verified move generation (startpos 20/400/8902, Kiwipete
48/2039/97862), castling / en passant / promotion handled.
Honest note: material-only depth 3 is a lottery ticket for "strongest engine", not a contender — it is a valid, legal entry.
