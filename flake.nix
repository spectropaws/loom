{
  description = "Loom - Agentic AI Environment Scaffolder";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python311
            uv

            # Tools
            git
            just
          ];

          shellHook = ''
            # Force uv to use the Nix-provided Python, not download its own
            export UV_PYTHON_DOWNLOADS=never
            
            # Point to the current folder's virtual environment
            export VIRTUAL_ENV=$PWD/.venv
            export PATH=$VIRTUAL_ENV/bin:$PATH

            echo "🚀 Forge Dev Environment"
            echo "   Python: $(python --version)"
            echo "   uv: $(uv --version)"
          '';
        };
      }
    );
}
