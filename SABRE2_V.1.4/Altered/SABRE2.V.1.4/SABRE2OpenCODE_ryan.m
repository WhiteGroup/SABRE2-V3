% function [JNodevalue,Massemble,JNodevalue_i,JNodevalue_j,Rval,BNodevalue,...
%    SNodevalue,RNCc,NCc,Nshe1,Nshe2,DUP1,DUP2,LNC,LNC1,LNC2,...
%    LUEC,PNC,PNC1,PNC2,BNC,BNC1,BNC2,FEL,AnalP]=SABRE2OpenCODE(data,vrum_az_slider,vrum_el_slider,...
%    vrum_az_edit,vrum_el_edit,axesm,vstm)
% Developed by Woo Yong Jeong.
% Date : 12/01/2012.
% ************************************************************************
% *****************           OPEN AND LOAD FILE      ********************
<<<<<<< HEAD:SABRE2_V.1.4/Altered/SABRE2.V.1.4/SABRE2OpenCODE_ryan.m
% ************************************************************************
file = 'C:\Users\rslein3\Desktop\SABRE2Calculator.V.1.4_Batch_Elastic_mod\input\case errors\rho02.mat'
data=load(file,'-ascii');
JNodevalue = data.JNodevalue; 
=======
% ************************************************************************ 
JNodevalue = data.JNodevalue 
>>>>>>> 6b28822d7139bc6b5a1ae2bd584aacb50f0cca1e:SABRE2_V.1.4/Altered/SABRE2.V.1.4/SABRE2OpenCODE.m
Massemble = data.Massemble;
disp(num2str(Massemble))
JNodevalue_i = data.JNodevalue_i
JNodevalue_j = data.JNodevalue_j
Rval = data.Rval
BNodevalue = data.BNodevalue
SNodevalue = data.SNodevalue
RNCc = data.RNCc
NCc = data.NCc
Nshe1 = data.Nshe1
Nshe2 = data.Nshe2;
DUP1 = data.DUP1;
DUP2 = data.DUP2;
LNC = data.LNC;
LNC1 = data.LNC1;
LNC2 = data.LNC2;
LUEC = data.LUEC;
PNC = data.PNC;
PNC1 = data.PNC1;
PNC2 = data.PNC2;
BNC = data.BNC;
BNC1 = data.BNC1;
BNC2 = data.BNC2;
FEL = data.FEL;
AnalP = data.AnalP;
% AnalP = [];
% Initially Auto Genetate BNodevalue for No Bracing Cases
if ~isempty(Massemble)
   if isempty(BNodevalue)
      mem = length(Massemble(:,1));
      for i = 1:mem
         BNodevalue(i,1,1)=i;
         BNodevalue(i,1,2)=0; % 0 No bracing
      end
   elseif ~isequal(length(Massemble(:,1)),length(BNodevalue(:,1,1)))
      mem = length(Massemble(:,1));
      bn = length(BNodevalue(:,1,1));
      for i = (bn+1):mem
         BNodevalue(i,1,1)=i;
         BNodevalue(i,1,2)=0; % 0 No bracing
      end
   end 
end   

SABRE2ModelP(JNodevalue,Massemble,JNodevalue_i,JNodevalue_j, ...
   Rval,BNodevalue,vrum_az_slider,vrum_el_slider,vrum_az_edit,vrum_el_edit,axesm,vstm);

% X-Y View
az = 0; el = 0; view(az, el);
set( gca, 'Units', 'normalized', 'Position', [0 0 1 1] );