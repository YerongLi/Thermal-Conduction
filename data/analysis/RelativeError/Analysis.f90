program main
  implicit none
  double precision,dimension(82289)::kappa1=0.d0,error1=0.d0,rerror1=0.d0
  double precision,dimension(82289)::kappa2=0.d0,error2=0.d0,rerror2=0.d0
  double precision,dimension(300)::ratio=0.d0
  integer::i=0,j=0,k=0,error=0
  real::r=0.0
  open(unit=1,file='KappaFile.dat',status='old',action='read')
  open(unit=2,file='ErrorFile.dat',status='old',action='read')
  open(unit=3,file='New.dat',status='old',action='read')
  open(unit=4,file='NewError.dat',status='old',action='read')
  open(unit=7,file='Comparison.dat',status='replace',action='write')
  do i=27428,1,-1
    read(1,*) kappa1(i)
    read(2,*) error1(i)
    read(3,*) kappa2(i)
    read(4,*) error2(i)
  enddo
    rerror1=error1/kappa1
    rerror2=error2/kappa2
  r=.023
  do i=0,30
    j=1
    do while (rerror1(j)<r)
      j=j+1
    enddo
    k=1
    do while (rerror2(k)<r)
      k=k+1
    enddo
    j=27429-j!!j is from Muller Plathe method
    k=27429-k!!k is from Philip's method
    write (7,100) r,real(k)/real(j),k,j
    r=r+0.001
  enddo
    100 format(f10.6,f17.12,2i10)
  close(unit=1)
  close(unit=2)
  close(unit=3)
  close(unit=4)
  close(unit=7)
end program main
