# let
#   # pkgs = import <nixpkgs> {};
#   mach-nix = import (builtins.fetchGit {
#     url = "https://github.com/DavHau/mach-nix/";
#     # place version number with the latest one from the github releases page
#     ref = "refs/tags/3.5.0";
#   }) {};
# in
# mach-nix.mkPython {
#   # python = pkgs.python38;
#   python = "python39";
#   # contents of a requirements.txt (use builtins.readFile ./requirements.txt alternatively)
#   requirements = builtins.readFile ./requirements.txt;
#   # requirements = builtins.readFile ./requirements_dev.txt;
# }

let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
  buildInputs = with pkgs; [ python39 poetry ];

  shellHook = ''
    # Needed for python packages that use c++ std library
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.stdenv.cc.cc.lib}/lib
    # Needed for numpy to use zlib.
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.zlib}/lib

    # Check if environment tool is initalized
    if [ -f poetry.lock ]; then
      poetry shell
    fi
    # if [ ! -d .venv ]; then
    #   python3 -m venv .venv
    #   source .venv/bin/activate
    #   python3 -m pip install --upgrade pip
    #   python3 -m pip install -r requirements.txt
    #   python3 -m pip install -r requirements_dev.txt

    #   # pulp vendors cbc and so it's interpretter needs patching
    #   patchelf \
    #     --set-interpreter "$(cat $NIX_CC/nix-support/dynamic-linker)" \
    #     ./.venv/lib/python3.9/site-packages/pulp/solverdir/cbc/linux/64/cbc
    # else
    #   source .venv/bin/activate
    # fi
  '';
}

# { pkgs ? import <nixpkgs> {} }:
# (pkgs.buildFHSUserEnv {
#   name = "TxGraffiti-dev";
#   targetPkgs = pkgs: (with pkgs; [
#     python39
#     python39Packages.pip
#     python39Packages.virtualenv
#   ]);
#   runScript = "bash";
# }).env
