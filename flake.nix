{
  description = "nix is love, nix is life";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    devshell.url = "github:numtide/devshell";
  };

  outputs = { self, nixpkgs, devshell, flake-utils }:
    let
      pkgsFor = system:
        import nixpkgs {
          inherit system;
          overlays = [ devshell.overlay ];
        };
      forAllDefaultSystems = f:
        flake-utils.lib.eachDefaultSystem (system: f system (pkgsFor system));
    in forAllDefaultSystems (system: pkgs: {
      devShell = pkgs.devshell.mkShell {
        imports = [ (pkgs.devshell.importTOML ./devshell.toml) ];
      };
    });
}
