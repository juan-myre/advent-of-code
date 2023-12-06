import { CompanyCreateBody, EntityDto, Shau } from "./classes";

console.log('juan bustamante');

const companyCreateBody: CompanyCreateBody = new CompanyCreateBody();
const shau: Shau = new Shau();

function passEntityDto(param: EntityDto) {
  console.log(param.id);
}

passEntityDto(shau);
