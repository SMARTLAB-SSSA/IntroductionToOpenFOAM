fvScalarMatrix TEqn
(
    fvm::div(phi,T)
    - fvm::laplacian(turbulence->nu()/Pr + turbulence->nut()/Prt,T)
    ==
    fvOptions(T)
);

TEqn.relax();
TEqn.solve();
